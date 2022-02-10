<html>
    <body>
        <?php
            $cmcDate = shell_exec('date "+%Y-%m-%d %H:%M:%S"');
            echo "<div>CMC Time : $cmcDate</div>";
            $rtcDate = substr(shell_exec('sudo hwclock -r'), 0, 19);
            echo "<div>RTC Time : $rtcDate</div>";

            $cmcTime = strtotime($cmcDate);
            $rtcTime = strtotime($rtcDate);
            $diff = abs($rtcTime - $cmcTime);

            echo "<div>Differnce : $diff sec</div>";

            if($rtcTime == false)
            {
                echo ("<div>RTC is not set</div>");
            }
            else if (diff < 60) {
                echo ("<div>difference below 1 minute</div>");
            }
            else {
                echo ("<div>difference above 1 minute</div>");
            }
        ?>
    </body>
</html>