CREATE TABLE hbnb_dev_db.places (
        city_id VARCHAR(60) NOT NULL,
        user_id VARCHAR(60) NOT NULL,
        name VARCHAR(128) NOT NULL,
        description VARCHAR(1024),
        number_rooms INTEGER,
        number_bathrooms INTEGER,
        max_guest INTEGER,
        price_by_night INTEGER,
        latitude FLOAT,
        longitude FLOAT,
        id VARCHAR(60) NOT NULL,
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(city_id) REFERENCES cities (id),
        FOREIGN KEY(user_id) REFERENCES users (id),
        UNIQUE (id)
);
