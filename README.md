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
    
    >> python3 manage.py migrate 
    (change python command based on the OS)  
    
    
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

    Implmented on rest api standards. Should be implmented in a stateless way, but for version 1 authentication is implmented with django auth token approch. Token is saved in db. 
    
        Enhancements : Implement authentication with jwt token
    
    port : 8000 . 
    
    
    Endpoints are secured and need to add Authentication token as below;
    
    1. Obtain the auth_token with authentication endpoint
    2. Add Auth header:
        Header name     :   Authorization
        Header value    :   Toke <auth_token>
        
URIs . 

1. Authentication  

        HTTP Method     :   POST                                  

        URI             :   /api/v1/authentication/   
        
        Request         :       {    
                                    "username": "django-admin",
                                    "password": "django-admin"

                                } 
        
        Response        :       {
                                    "token": "5384d782a77100000003f3c14e80977f47e8659",
                                    "user_id": 1,
                                    "email": "test@gmail.com"
                                }          
                                
2. Logout
         
        HTTP Method     :   POST                                  

        URI             :   /api/v1/logout/   
        
        Request         :   No Body
        
                            Header => Authorization : Token <tokenvalue>
        
        Response        :       {
                                    "success": "Successfully logged out."
                                } 
                                
                                
3. List Tournaments
         
        HTTP Method     :   GET                                  

        URI             :   /api/v1/tournaments/ 
        
        Request         :   -
        
                            Header => Authorization : Token <tokenvalue>
        
        Response        :       [
                                    {
                                        "id": 2,
                                        "name": "Shgner Cup",
                                        "identifier": "Shgner2024",
                                        "mascot": "Mow Mow"
                                    },
                                    {
                                        "id": 1,
                                        "name": "Wilson International World Cup",
                                        "identifier": "WilsCup2024",
                                        "mascot": "Crazy Frog"
                                    }
                                ]
                                
4. List Games for Tournament
         
        HTTP Method     :   GET                                  

        URI             :   /api/v1/tournaments/<tournamentid>/games
        
        Request         :   -
        
                            Header => Authorization : Token <tokenvalue>
        
        Response        :       [
                                    {
                                        "id": 2,
                                        "game_level": "QU",
                                        "teams": "tre vs tyr",
                                        "game_status": "PL",
                                        "game_time": "2024-06-21 00:00:00"
                                    },
                                    {
                                        "id": 3,
                                        "game_level": "QU",
                                        "teams": "wer vs dse",
                                        "game_status": "CR",
                                        "game_time": "2024-06-20 00:00:00"
                                    },
                                    {
                                        "id": 1,
                                        "game_level": "QU",
                                        "teams": "wer vs dse",
                                        "game_status": "SC",
                                        "game_time": "2024-06-19 00:00:00"
                                    },
                                    {
                                        "id": 4,
                                        "game_level": "QU",
                                        "teams": "tre vs tyr",
                                        "game_status": "CR",
                                        "game_time": "2024-06-19 00:00:00"
                                    }
                                ]
                                
5. Tournament Scoreboard
         
        HTTP Method     :   GET                                  

        URI             :   /api/v1/tournaments/<tournamentid>/scoreboard
        
        Request         :   -
        
                            Header => Authorization : Token <tokenvalue>
        
        Response        :       [
                                    {
                                        "id": 2,
                                        "game_level": "QU",
                                        "teams": "tre vs tyr",
                                        "game_status": "PL",
                                        "game_time": "2024-06-21 00:00:00"
                                    },
                                    {
                                        "id": 3,
                                        "game_level": "QU",
                                        "teams": "wer vs dse",
                                        "game_status": "CR",
                                        "game_time": "2024-06-20 00:00:00"
                                    },
                                    {
                                        "id": 1,
                                        "game_level": "QU",
                                        "teams": "wer vs dse",
                                        "game_status": "SC",
                                        "game_time": "2024-06-19 00:00:00"
                                    },
                                    {
                                        "id": 4,
                                        "game_level": "QU",
                                        "teams": "tre vs tyr",
                                        "game_status": "CR",
                                        "game_time": "2024-06-19 00:00:00"
                                    }
                                ]
                                
6. List teams
         
        HTTP Method     :   GET                                  

        URI             :   /api/v1/teams
        
        Request         :   -
        
                            Header => Authorization : Token <tokenvalue>
        
        Response        :       [
                                    {
                                        "id": 1,
                                        "name": "Black Panthers",
                                        "displayname": "BLKP",
                                        "slogan": "U Can't C M@",
                                        "rank": 1
                                    },
                                    {
                                        "id": 10,
                                        "name": "Boston Celtics",
                                        "displayname": "BSCT",
                                        "slogan": "Yeah",
                                        "rank": 10
                                    },
                                    {
                                        "id": 9,
                                        "name": "Country sides",
                                        "displayname": "CSDS",
                                        "slogan": "Yes We are",
                                        "rank": 9
                                    },
                                    .
                                    .
                                    .
                                    .
                                    {
                                        "id": 3,
                                        "name": "West Indies Super10",
                                        "displayname": "WIS10",
                                        "slogan": "From Windies",
                                        "rank": 3
                                    }
                                ]
           
        
    

    
    
    
    
    