## Topic 04 – Database with SQLAlchemy

- ORM concepts
- Database connection
- Models & schemas
- Dependency-based DB session
- CRUD with SQLAlchemy

### Code explanation

## 1. database.py
   
   . create_engine -> Create DB connection.
   . sessionmaker -> DB session (talking with DB)
   . declarative_base -> base class for tables.
   . SQLite database
   . ./test.db -> DB file in the Project
   . engine -> actual DB connection
   . check_same_thread=False -> required for SQLite FastAPI
   . Session -> connection with DB
   . autocommit = False -> maually commit
   . autoflush= False -> control flush
   
## 2. schemas.py

    .orm_mode = True -> SQLAlchemy object -> JSON

## 3. main.py
 
    . add() -> add record
    . commit() -> save
    .refresh() -> get ID from DB
