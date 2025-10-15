# Temperature Simulator

## Description
A program szimulál egy egyszerű hőmérsékletérzékelő rendszert, amely képes:
véletlenszerű hőmérséklet értékeket generálni,
ezeket elküldeni egy ROS2 topic-ra,
és egy másik node-ban feldolgozni, valamint kiértékelni, hogy az érték normális, túl magas vagy túl alacsony.

A csomag neve: `temp_ros_pkg` amely két node-ból áll a `temperature_publisher` amely véletlenszerű hőmérséklet adatokat generál és publikálja az adatokat egy `/temperature` topic-ra. A második node pedig a `temperature_subscriber` amely feliratkozik a `/temperature` topic-ra és kiírja a mért értéket, és figyelmeztet, ha az eltér a normál tartománytól.


## Package & Build

...