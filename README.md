"blms" application for basketball league management Provides below features:

    1. League related
    * Tournament data
    * Games for tournament
    * Coaches
    * Teams
    * Players
    * Dashboard with game results
    * Player stats
    * Team stats
    
    2. Authentication and autherization
    * Retrive auth token with username / password
    * Token based autherization for endpoits (Authorization header token)
    * Team data restrictiononly for coach of the team
    * User stat view for admin
    
How to run

Python version used : 3.11.6
DB : SQLite


1. Checkout the repository;
    >> git clone https://github.com/priyanga220/matific_blms.git
    
2. cd into the folder
    >> cd matific_blms
    
3. Use the branch "feature/testDataWithApiAndAdminPanel" 

    >> git checkout feature/testDataWithApiAndAdminPanel
    
4. Apply requirments
    
    >> pip3 install -r requirements.txt
    
5. CD into the Project folder (blms) and Run migrations to apply changes and to create DB 
    >> cd blms
    >> python3 manage.py migrate (python command change based on the OS)
    
    This will create the required DB schema. (db.sqlite3)
    
6. Load the test data from "testdata.json" file. This is located in core application inside fixtures folder

    >> python3 manage.py loaddata core/fixtures/testdata.json
    
        This will create some sample data including users to test the application:
        
            * Admin user - this user is django super user with application role "Admin"
                username : django-admin, password : django-admin
                
            * Role : Coach
                username : coach1, password : Djpwd123
                username : coach2, password : Djpwd123
                
            * Role : Player
                username : Player1, password : DJPwd123
    
7. Run the application

    >> python3 manage.py runserver
    
        * django admin panel  ==> http://localhost:8000/admin/ 
        (username : django-admin, password : django-admin)
    
    
ER Diagram 

    * core_* tables for blms application data (core_tournament, core_team, core_game, core_coach, core_player, core_playerstat, core_gamestat)
    
    * auth_* tables from django framework for user and authentication management combined with core_userrole and core_userstat tables
    
        1. Create (add) the user from django-admin panel -> this will create the auth_user entry
        2. Add new entry in User roles table
            Content-type    :   For Admin role  ->   Select "Authentication and Autherization | user" option
                                For Coach role  ->   Select "Core | coach" option
                                For Player role ->   Select "Core | player" option
                                
            Object id       :   Select the relavant table entry id 
                                (Admin -> auth_user table , Coach -> core_coach table, Player -> core_player table)
                
            Userrole        :   Select the Role
            
            User            :   Select the user which needs to assign the role
    
    
    
    


Endpoints

    Implmented on rest api standards.
    
    Endpoints are secured and need to add Authentication token as below;
    
    1. Obtain the auth_token with authentication endpoint
    2. Add Auth header:
        Header name     :   Authorization
        Header value    :   Toke <auth_token>

    
    
    
    
    