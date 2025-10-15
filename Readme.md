# Temperature Simulator

## Description
A program szimulál egy egyszerű hőmérsékletérzékelő rendszert, amely képes:
véletlenszerű hőmérséklet értékeket generálni,
ezeket elküldeni egy ROS2 topic-ra,
és egy másik node-ban feldolgozni, valamint kiértékelni, hogy az érték normális, túl magas vagy túl alacsony.

A csomag neve: `temp_ros_pkg` amely két node-ból áll a `temperature_publisher` amely véletlenszerű hőmérséklet adatokat generál és publikálja az adatokat egy `/temperature` topic-ra. A második node pedig a `temperature_subscriber` amely feliratkozik a `/temperature` topic-ra és kiírja a mért értéket, és figyelmeztet, ha az eltér a normál tartománytól.


## Package & Build


``` bash
source install/local_setup.bash
```
</details>

``` terminal 1
ros2 run temp_ros_pkg temperature_publisher
```

``` terminal 2
ros2 run temp_ros_pkg temperature_subscriber
```

## Graph

```mermaid
graph LR;

publisher([ temperature_publisher ]):::red --> temperature;
temperature[ /temperature<br/>std_msgs/Float64 ]:::light --> subscriber([ temperature_subscriber ]):::red;

classDef light fill:#34aec5,stroke:#152742,stroke-width:2px,color:#152742 
classDef dark fill:#152742,stroke:#34aec5,stroke-width:2px,color:#34aec5
classDef white fill:#ffffff,stroke:#152742,stroke-width:2px,color:#152742
classDef red fill:#ef4638,stroke:#152742,stroke-width:2px,color:#fff
