create table Players (
    id SERIAL PRIMARY KEY,
    name Varchar(255),
    player_state Varchar(50), --in game/in lobby / offline
    statistic JSONB
    
)

create table Lobbies (
    id SERIAL PRIMARY KEY ,
    lobby_maker INT REFERENCES Players(id) ,
    player_status VARCHAR(50) ,
    settings_match JSONB
)


create table Games (
    id_lobby INT PRIMARY KEY REFERENCES Lobbies(id),
    game_status VARCHAR(50),
    current_position INT,
    time_start TIMESTAMP 
)

create table Teams (
    id SERIAL PRIMARY KEY,
    game_id INT REFERENCES Games(id_lobby),
    name VARCHAR(255),
    color VARCHAR(10),так
    role VARCHAR(50)
)

create table LobbyPlayers (
    id SERIAL PRIMARY KEY,
    lobby_id INT REFERENCES Lobbies(id),
    player_id INT REFERENCES  Players(id),
    team_id INT REFERENCES Teams(id)
)

create table GamePlayers(
    id SERIAL PRIMARY KEY,
    game_id INT REFERENCES Games(id_lobby),
    player_id INT REFERENCES Players(id),
    team_id INT REFERENCES Teams(id)
)

