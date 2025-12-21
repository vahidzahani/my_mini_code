<?php
$fileStats = []; // File extension statistics
$totalFiles = 0;
$totalLines = 0;
$displayContent = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $paths = explode("\n", $_POST['file_paths']); // Get file paths line by line
    $displayContent .= "<div style='font-family: monospace;'>";
    
    foreach ($paths as $path) {
        $path = trim($path);
        // Remove quotes from path
        $path = str_replace(['"', "'"], '', $path);

        if (file_exists($path) && is_file($path)) {
            $totalFiles++;
            $lines = file($path, FILE_IGNORE_NEW_LINES); // Read file line by line
            $lineCount = count($lines);
            $totalLines += $lineCount;

            // Get file extension
            $ext = pathinfo($path, PATHINFO_EXTENSION);
            if ($ext === '') $ext = 'no_extension';
            if (!isset($fileStats[$ext])) $fileStats[$ext] = 0;
            $fileStats[$ext]++;
            
            $displayContent .= "===========================================================================<br>";
            $displayContent .= "<h3 style='color: blue;'><a href='file:///$path' target='_blank'>$path</a></h3>";
            $displayContent .= "===========================================================================<br>";
            $displayContent .= "<pre>" . htmlspecialchars(implode("\n", $lines)) . "</pre><hr>";
        } else {
            //$displayContent .= "<h3 style='color: red;'>$path</h3>";
            //$displayContent .= "<p style='color:red;'>File does not exist or path is incorrect.</p><hr>";
        }
    }
    
    $displayContent .= "</div>";
}
?>

<form method="post">
    <textarea name="file_paths" rows="15" cols="80"
        placeholder="Enter file paths here"><?= isset($_POST['file_paths']) ? htmlspecialchars($_POST['file_paths']) : '' ?></textarea><br>
    <button type="submit">Display File Contents</button>
</form>

<?php if ($_SERVER['REQUEST_METHOD'] === 'POST'): ?>
    <h2>Overall Statistics</h2>
    <p>Total files: <?= $totalFiles ?></p>
    <p>Total lines: <?= $totalLines ?></p>

    <?php if (!empty($fileStats)): ?>
        <h3>File Count by Extension</h3>
        <table border="1" cellpadding="5" cellspacing="0">
            <tr>
                <th>File Extension</th>
                <th>Count</th>
            </tr>
            <?php foreach ($fileStats as $ext => $count): ?>
                <tr>
                    <td><?= htmlspecialchars($ext) ?></td>
                    <td><?= $count ?></td>
                </tr>
            <?php endforeach; ?>
        </table>
    <?php endif; ?>

    <h2>File Contents</h2>
    <?= $displayContent ?>
<?php endif; ?>
