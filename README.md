# Belief Revision Artificial Intelligence

## Execution
It is required to have python3.x version

To execute the program open a terminal in the folder beliefRevision that contains
the files BeliefRevisionAgent.py and testAgent.py and execute testAgent.py:

`python testAgent.py`

or

`python3 testAgent.py`

## Usage
The program will execute and print the initial empty Belief Base in CNF. Then it is asked to input new information which is 
necessary to be a clause of disjuntions and press enter (disjunction represented as 'v' or 'V' and negated literals with a  '-' 
before them) for 
example:

a V -b

After pressing enter, AGM revision will be done and the new Belief Set will be printed in screen.

You can add as much as new clauses as wanted, i.e:
```
Belief Base = {}

Enter new Info: a V b

Updated new Belief set:
Belief base:= {{a V b} }

Enter new Info: -c
 
Updated new Belief set:
Belief base:= {{a V b}, {-c} }
```
To exit the program press ctrl + c
