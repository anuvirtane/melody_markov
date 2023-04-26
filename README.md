# melody_markov

Helsinki university Algorithms and data structures student project. 

[Project definition](documentation/project_definition.md)

[Week 1 progress report](documentation/progress_report_week_1.md)

[Week 2 progress report](documentation/progress_report_week_2.md)

[Week 3 progress report](documentation/progress_report_week_3.md)

[Week 4 progress report](documentation/progress_report_week_4.md)

[Week 5 progress report](documentation/progress_report_week_5.md)

[Week 6 progress report](documentation/progress_report_week_6.md)

[Test coverage report](https://anuvirtane.github.io/melody_markov/)

[Test documentation](documentation/testing.md)

If you have Python and Poetry installed, you can run project.


### Install dependencies 

    poetry install


### Run very basic version of application without GUI

    poetry run invoke start

### Run all unit tests

    poetry run invoke coverage

### Generate test coverage report


First navigate to src folder

    cd src

Then run command

    poetry run invoke coverage-report

Coverage report is then generated in htmlcov folder inside src folder