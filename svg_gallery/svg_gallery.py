import os
from pathlib import Path
import re

base_dir = Path(".").resolve()

def log(message):
    print(f"[LOG] {message}")

def fix_svg_size(svg_text):
    """
    Modify <svg> tag to have width=100 height=100 and preserveAspectRatio="none"
    to force stretch.
    """
    match = re.search(r'<svg\b[^>]*>', svg_text, flags=re.IGNORECASE)
    if not match:
        return svg_text

    svg_tag = match.group(0)

    # Remove width, height, preserveAspectRatio attributes if exist
    svg_tag_fixed = re.sub(r'\swidth="[^"]*"', '', svg_tag, flags=re.IGNORECASE)
    svg_tag_fixed = re.sub(r'\sheight="[^"]*"', '', svg_tag_fixed, flags=re.IGNORECASE)
    svg_tag_fixed = re.sub(r'\spreserveAspectRatio="[^"]*"', '', svg_tag_fixed, flags=re.IGNORECASE)

    # Add width, height and preserveAspectRatio="none"
    if svg_tag_fixed.endswith('/>'):
        svg_tag_fixed = svg_tag_fixed[:-2] + ' width="100" height="100" preserveAspectRatio="none" />'
    else:
        svg_tag_fixed = svg_tag_fixed[:-1] + ' width="100" height="100" preserveAspectRatio="none">'

    fixed_svg_text = svg_text[:match.start()] + svg_tag_fixed + svg_text[match.end():]

    return fixed_svg_text

def create_gallery(folder: Path, svg_files: list[Path]):
    html_path = folder / "gallery.html"
    log(f"Creating gallery.html in '{folder.relative_to(base_dir)}' with {len(svg_files)} SVG files...")

    with open(html_path, "w", encoding="utf-8") as f:
        f.write("<html><head><title>SVG Gallery</title></head><body>\n")
        f.write(f"<h1>Gallery: {folder.name}</h1>\n")

        for svg in svg_files:
            if not svg.exists():
                log(f"[WARNING] File not found: {svg}")
                continue
            try:
                with open(svg, "r", encoding="utf-8") as svg_file:
                    svg_content = svg_file.read()
                svg_content_fixed = fix_svg_size(svg_content)

                f.write("<div style='width:100px; height:100px; overflow:hidden; border:1px solid #ccc; margin:10px; display:inline-block;'>\n")
                f.write(svg_content_fixed)
                f.write("</div>\n")
            except Exception as e:
                log(f"[ERROR] Failed to read {svg}: {e}")
                continue

        f.write("</body></html>")

    log(f"✅ gallery.html created at: {html_path}")

def create_index(galleries: list[tuple[Path, Path]]):
    index_path = base_dir / "index.html"
    log("Creating index.html...")

    with open(index_path, "w", encoding="utf-8") as f:
        f.write("<html><head><title>SVG Galleries</title></head><body>\n")
        f.write("<h1>SVG Galleries</h1>\n")

        for folder, sample_svg in galleries:
            gallery_url = folder.as_posix() + "/gallery.html"
            f.write("<div style='margin:10px; display:inline-block; border:1px solid #ccc; width:100px; height:100px; overflow:hidden;'>\n")
            f.write(f"<a href='{gallery_url}' target='_blank' style='display:block; width:100%; height:100%;'>\n")
            try:
                with open(base_dir / sample_svg, "r", encoding="utf-8") as svg_file:
                    svg_content = svg_file.read()
                svg_content_fixed = fix_svg_size(svg_content)
                f.write(svg_content_fixed)
            except Exception as e:
                log(f"[ERROR] Could not embed preview SVG {sample_svg}: {e}")
                f.write(f"[Preview Error: {e}]")
            f.write("</a></div>\n")

        f.write("</body></html>")

    log(f"✅ index.html created at: {index_path}")

def main():
    log("[1/4] Scanning folders...")
    galleries_info = []

    for root, dirs, files in os.walk(base_dir):
        folder = Path(root)
        svg_files = [folder / f for f in files if f.lower().endswith(".svg")]
        if len(svg_files) > 5:
            log(f"✅ '{folder.relative_to(base_dir)}' has {len(svg_files)} SVG files.")
            create_gallery(folder, svg_files)
            galleries_info.append((
                folder.relative_to(base_dir),
                svg_files[0].relative_to(base_dir)
            ))
        else:
            log(f"Skipping '{folder.relative_to(base_dir)}' ({len(svg_files)} SVG files).")

    if galleries_info:
        log("[2/4] Galleries generated.")
        create_index(galleries_info)
        log("[3/4] index.html created.")
    else:
        log("❌ No folders with more than 5 SVG files found. Skipping index.html.")

    log("[4/4] Done.")

if __name__ == "__main__":
    main()
