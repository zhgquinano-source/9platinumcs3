# Class Attributes and Methods

## Previous Design
Link to my previous activity:
[classObjectUML.md](q1/classObjectUML.md)

## Design Revision
No major changes were needed from my original design.

## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
| --------- | --------- | ---------- | ------ |
| songName  | string    | Public     | Users need to identify the song. |
| genre     | string    | Public     | Users may need to know or access the song genre. |
| duration  | int       | Private    | The duration should be protected from invalid values. |
| album     | string    | Public     | Users may need to know which album the song belongs to. |
| artist    | string    | Public     | Users need to know who created the song. |

## Updated UML Class Diagram
[Class Diagram](classDiagramSG5.png)

## Python Implementation
[View Python Source](classImplementation.py)

## Test Run
[Test Run](classTestRun.png)

## Object Diagram
[Object Diagram](objectDiagram.png)


## Analysis
### Why did you make your chosen attribute private?
I made `duration` private because a song’s duration should not be changed directly. This prevents invalid values, such as negative or unrealistic durations. The `change_duration()` method controls changes and ensures the new duration is greater than zero.

### Which method changes the state of your object?
The `change_duration()` method changes the state of my `Songs` object by updating the private `duration` when the new value is valid. For example, Object 1 changes from 210 to 240 seconds, while Object 2 keeps its original duration.

### How did your two objects demonstrate that instances are independent?
My two objects were created from the same `Songs` class but had different values. When I changed the duration of Object 1, only Object 1's duration changed. Object 2 kept its original duration, showing that each object has its own separate attributes.

### What is the difference between your class diagram and your object diagram?
The class diagram shows the blueprint of the `Songs` class, including its attributes, data types, visibility, and methods. The object diagram shows the actual objects created from it, including their stored values. It also shows the final values after Object 1 was changed.
