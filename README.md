Expt
====

A program to manage and store experiments performed in proper folders. It also generates reports and summaries.

A report is a fully detailed text for all the experiments in bench/archive or both. A summary on the other hand is a smaller version which let's you get an overview quickly.

Why?
----

Handling experiments as notebooks becomes unwieldly very quickly. You lose track of what you were working on and what needs work.


How?
----

You start a new hypothesis based experiment. The software creates a new directory for you rooted in the current directory. It starts up a new jupyter notebook for this purpose. You can close and exit safely. You can continue to work on different hypothesis separately.

Folder Structure
---------

```
-experiments
    |
    |\__REPORT
    |
    |\__SUMMARY
    |
    |
    |\___expt1
    |       |
    |       |\__meta.json
    |       |\__notes.json
    |        \__notebook.ipynb
    |
    |
    |\___expt2
    |       |
    |       |\__meta.json
    |       |\__notes.json
    |        \__notebook.ipynb
    |
    |
     \___expt3
            |
            |\__meta.json
            |\__notes.json
             \__notebook.ipynb
Usage
-----

```bash
cd ~/experiments
expt list <all>
```
- `expt new <hypothesis title>` creates a new expt
- `expt work <hypothesis blob>` start jupyter server in said expt
- `expt note <hypothesis blob> <message>` creates a new note in the give blob
- `expt stop <hypothesis blob>` stops work in an expt
- `expt archive <hypothesis blob>` compresses and stores the expt folder in archives
- `expt summary` creates a summary of expts currently in bench
- `expt report` creates a summary of expts currently in bench


Todo
----

- [x] list
- [x] new
- [x] work
- [x] note
- [x] stop
- [ ] summary
- [ ] report
- [ ] archive
- [ ] Brow archive
