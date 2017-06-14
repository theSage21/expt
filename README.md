Expt
====

A program to manage and store experiments performed.

Why?
----

Handling experiments as notebooks becomes unwieldly very quickly. You lose track of what you were working on and what needs work.


How?
----

You start a new hypothesis based experiment. The software creates a new directory for you rooted in the current directory. It starts up a new jupyter notebook for this purpose. You can close and exit safely. You can continue to work on different hypothesis separately.

Usage
-----

```bash
cd ~/experiments
expt list
expt new <hypothesis title> <id>
expt work <hypothesis id>
expt note <hypothesis id> <message>
expt stop <hypothesis id>
expt archive <hypothesis id>
expt summary
expt report
```
