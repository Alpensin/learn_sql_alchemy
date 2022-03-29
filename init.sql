
CREATE TABLE users (
	id SERIAL NOT NULL,
	username VARCHAR(100) NOT NULL,
	email VARCHAR(100) NOT NULL,
	password VARCHAR(200) NOT NULL,
	CONSTRAINT user_pk PRIMARY KEY (id),
	UNIQUE (username),
	UNIQUE (email)
);

CREATE TABLE posts (
	id SERIAL NOT NULL,
	title VARCHAR(100) NOT NULL,
	slug VARCHAR(100) NOT NULL,
	content VARCHAR(50) NOT NULL,
	published VARCHAR(200) NOT NULL,
	user_id INTEGER NOT NULL,
	created_on TIMESTAMP WITHOUT TIME ZONE,
	updated_on TIMESTAMP WITHOUT TIME ZONE,
	PRIMARY KEY (id),
	FOREIGN KEY(user_id) REFERENCES users (id)
);

INSERT INTO users (username, email, password)
VALUES
       ('ranger', 'ranger@ya.ru', '1'),
       ('flint', 'flint@ya.ru', '2'),
       ('zizy', 'zizy@ya.ru', '2'),
       ('zorg', 'zorg@ya.ru', 'asdasd'),
       ('roberto', 'roberto@ya.ru', 'asd'),
       ('alehandro', 'alehandro@ya.ru', 'd'),
       ('fernando', 'fernando@ya.ru', 'ddd')
;
INSERT INTO posts (title, slug, content, published, user_id)
VALUES
       ('summer', 'sum', 'was hot', 'yep', 1),
       ('autumn', 'aut', 'was rainy', 'yes', 2),
       ('winter', 'win', 'was cold', 'da', 3),
       ('spring', 'spr', 'was nice', 'si', 3)
;
