# Interview Challenge

## Description

Your project is to build a website that allows users to lookup information about vehicles by entering a Vehicle Serial Number (VSN).

The site should validate the VSN for proper formatting, and display the user a set of matched results, if any.


##### Included VSN Data Structure (.csv):

```

VSN Pattern, Vehicle Trim Id, Year, Make, Model, Trim Name

```


### VSN Matching:

- Valid VSNs are in the format of six letters (A-Z) followed by six numbers (0-9)
- VSN patterns contain exact-match characters (A-Z and 0-9) and wildcard characters (*). Any character of the valid type (as defined in #1) will match against a wildcard character
- If multiple patterns match the input, use the pattern that has more exact-match characters

##### Examples:
```

Pattern: "ABC*EF*****6" matches against "ABCAEF111116", but not "ABC1EFAAAAA6"

If there are two patterns: "ABCDEF******" and "ABCDEF1*****", the string "ABCDEF123456" would match against the second pattern because it has fewer asterisks.

```

### Client Specifications:

- At a minimum, the user interface should provide an input box to allow entry of the serial number, and a button to submit. If the serial number is invalid (does not match rule #1 above), show an error message to the user.

- This page can be very basic. It does not need any other special formatting other than to be valid, well-structured HTML (unless you feel like snazzing it up =).

- Write this website using any programming language of your choice, and feel free to use any third-party CSS or JS libraries.

### Evaluation

- You will be evaluated on all aspects of your solution, but we will focus on your ability to design and write code, and to make appropriate library choices for a production environment.

### Considerations

- Finally, while the VSN input set is relatively small, in a real-world environment the list will be much larger. If your solution would not adequately perform with tens or hundreds of thousands of VSN search patterns, please describe how you would build a solution to handle that in a readme file. The readme should also include any special installation requirements, known issues, areas for improvement, ideas for version 2, etc.


## Running the Application

1. Clone the rpository from GitHub
2. Spin up API:
    1. Install cassandra and CQLSH
        * For OSX:
            * ```brew update; brew install cassandra```
        * For Linux Debian/Ubuntu:
            * ```apt-get update; sudo apt-get install cassandra```
        * Please note these cassandra distributions are meant for testing only, for documentation on a full cassandra instillation please see [Apache Cassandra Documentation](https://wiki.apache.org/cassandra/GettingStarted) or [DataStax Community Documentation](http://planetcassandra.org/cassandra/)
    2. Start cassandra in terminal as a background process as follows:

        ```
        cassandra
        ```

        * The process has launched when 'state jump to normal', press enter to resume in your terminal
    3. Start CQLSH and run migrations:
        * Naviget to ```Interview/API/utils/migrations```
        * Create keyspace and table schema:

            ```sql
            cqlsh -f create_tc_keyspace.cql;
            cqlsh -f create_lookup_tables.csv
            ```

        * Cassnadra db is now completed, feel free to look around by envoking cqlsh and typing the following:

            ```sql
            DESCRIBE TABLE tc.vehicle_by_serial_number;
            ```

    3. Create Python3 Environment:
        * Make sure you have Python3.4 installed, if not visit [Python installation documentation](https://www.python.org/downloads/) and download the latest version of Python3
        * Naviget to ```Interview/API```
        * Create a Python3 virtualenvironment:

            ```
            python3 -m venv env
            ```

        * Start the virtual environment with:

            ```
            source env/bin/activate
            ```

        * Install application requirements to that virtual machine:

            ```
            pip3.4 install -r requirements.txt
            ```

        * Invoke data import within the Python3 Repl:

            ```python
            from utils.data.csv_reader import CSVReader
            CSVReader()
            ```

        * Your table should now be populated with data
   4. Start the application in the foreground as follows:

        ```
        python3 run.py
        ```

3. Spin up the Client:
    1. Make sure appropriate packages are installed:
        * Please see [NPM Download and Instillation Guide](https://nodejs.org) for instillation help with NPM
        * Install Bower:

            ```
            npm install bower #sudo may be necessary depending on environment
            ```

    2. In a new terminal, navigate to ```Interview/Client```
    3. Install all NPM dependencies:

        ```
        npm install #sudo may be necessary depending on environment
        ```

    4. Install all Bower dependencies:

        ```
        bower install
        ```

    5. Launch test server:

        ```
        grunt serve
        ```

    6. Local web server is now active, navigate to the website on the test server at ```http://localhost:9000/app/index.html```


## Comments

- Version 1 of the software uses a redimentary search and result aggregation algorithm, version 2 will insted use ElasticSearch and transition away from cassandra die to cassnadra-river problems.

- The current search algorithm and database schema are created from provided data where the first 4 of the VSN are always required, should that change for other vehicles, the schema and some logic would have to change

- This solution could be scaled to production size and provide a truly distributed database and quick lookups with locality considerations. All that would need to change are the cluster IP's in config.py and the possible addition of cassandra username and password for protected data stores.
