# Class Relationships: Association and Multiplicity

## Previous Work
[Part I - Classes and Objects](classObjectUML.md)

[Part II - Class Attributes and Methods](classAttributesMethods.md)

## Existing Class
Class: Songs
Description: A song is a short piece of music with words that people sing

## New Related Class
Class: Music Artists

Description: Music Artist/s are people/person who created song

## Association
Relationship: Songs HAS-AN Artist

Explanation: Every song has an artist because a song cannot exist when there's no one to produce it.

## Multiplicity
Multiplicity: 1..*

Explanation: Songs can have more than one artists(example: collabs) but can never have less than one artist/s.

## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)

## Python Implementation
[View Python Source](classRelationships.py)

## Test Run
![Relationship Test Run](images/relationshipTestRun.png)

## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)

## Analysis
### What is the association between your two classes? 
The artist/s creates the song and the song is the art the artist/s made

### What multiplicity did you choose and why? 
1 or more because a song can have more than 1 artist

### How did you implement the relationship in Python?

### Why did you store an object reference instead of copying its data?

### If your relationship uses many, why is a list appropriate?
