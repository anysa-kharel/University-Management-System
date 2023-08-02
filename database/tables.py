import mysql.connector

# Function to establish a connection to the MySQL server
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="uni_mngt_sys"
    )

# Function to execute a single SQL
def execute(connection,query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()

# Function to create the tables
def create_tables():
    try:
        # Connect to the MySQL server
        connection = create_connection()

        # Create the Lecturer table
        lecturer_table = '''
            CREATE TABLE Lecturer (
                LecturerNumber VARCHAR(10) PRIMARY KEY,
                LecturerName VARCHAR(255) NOT NULL,
                RoomNumber VARCHAR(10) NOT NULL
            )
        '''
        execute(connection, lecturer_table)

        # Create the Module table
        module_table = '''
            CREATE TABLE Module (
                ModuleCode VARCHAR(10) PRIMARY KEY,
                ModuleName VARCHAR(255) NOT NULL,
                Organized_by VARCHAR(10),
                FOREIGN KEY (Organized_by) REFERENCES Lecturer(LecturerNumber)
            )
        '''
        execute(connection, module_table)

        # Create the Lecture table
        lecture_table = '''
            CREATE TABLE Lecture (
                LectureID INT PRIMARY KEY,
                Time VARCHAR(10) NOT NULL,
                Room VARCHAR(10) NOT NULL,
                Day VARCHAR(10) NOT NULL,
                ModuleCode VARCHAR(10),
                FOREIGN KEY (ModuleCode) REFERENCES Module(ModuleCode)
            )
        '''
        execute(connection, lecture_table)

        # Create the Student table
        student_table = '''
            CREATE TABLE Student (
                StudentNumber VARCHAR(10) PRIMARY KEY,
                StudentName VARCHAR(255) NOT NULL
            )
        '''
        execute(connection, student_table)

        # Create the Lecture_Tutor table
        lecture_tutor_table = '''
            CREATE TABLE Lecture_Tutor (
                LectureID INT PRIMARY KEY,
                LecturerNumber VARCHAR(10),
                FOREIGN KEY (LectureID) REFERENCES Lecture(LectureID),
                FOREIGN KEY (LecturerNumber) REFERENCES Lecturer(LecturerNumber)
            )
        '''
        execute(connection, lecture_tutor_table)

        # Create the Tutor table
        tutor_table = '''
            CREATE TABLE Tutor (
                LecturerNumber VARCHAR(10),
                StudentNumber VARCHAR(10),
                FOREIGN KEY (LecturerNumber) REFERENCES Lecturer(LecturerNumber),
                FOREIGN KEY (StudentNumber) REFERENCES Student(StudentNumber)
            )
        '''
        execute(connection, tutor_table)

        #Create the Attendance Table
        attend_table= '''
            CREATE TABLE Attend (
                StudentNumber VARCHAR(10),
                LectureID INT,
                PRIMARY KEY (StudentNumber, LectureID),
                FOREIGN KEY (LectureID) REFERENCES Lecture(LectureID),
                FOREIGN KEY (StudentNumber) REFERENCES Student(StudentNumber)
            )
        '''
        execute(connection, attend_table)

        # Create the Registration table
        registration_table = '''
            CREATE TABLE Registration (
                RegistrationID INT PRIMARY KEY,
                StudentNumber VARCHAR(10),
                ModuleCode VARCHAR(10),
                RegistrationDate DATE,
                FOREIGN KEY (StudentNumber) REFERENCES Student(StudentNumber),
                FOREIGN KEY (ModuleCode) REFERENCES Module(ModuleCode)
            )
        '''
        execute(connection, registration_table)

        print("Tables created successfully!")

    except mysql.connector.Error as error:
        print("Error:", error)

    finally:
        if connection.is_connected():
            connection.close()

# Call the function to create the tables
create_tables()