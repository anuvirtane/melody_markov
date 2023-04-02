# melody_markov

Helsinki university Algorithms and data structures student project. 

[Project definition](documentation/project_definition.md)

[Week 1 progress report](documentation/progress_report_week_1.md)

[Week 2 progress report](documentation/progress_report_week_2.md)

[Week 3 progress report](documentation/progress_report_week_3.md)

[Test coverage report](https://anuvirtane.github.io/melody_markov/) from last week. Did not get it to work this week.

[Test documentation](documentation/testing.md)

If you have Python and Poetry installed, you can run project.

Install dependencies with command

    poetry install

To run unit tests start poetry shell with command

    poetry shell

Then use command

    pytest src

Generate test coverage report (while not in poetry shell) using command

    poetry run invoke coverage
