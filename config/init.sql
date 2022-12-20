CREATE DATABASE Exams;

\c exams;

CREATE TABLE tests (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    picture_path VARCHAR(255) NOT NULL
);


CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    content VARCHAR(255) NOT NULL,
    picture_path VARCHAR(255) NOT NULL,
    test_id INT NOT NULL REFERENCES tests(id)
);


CREATE TABLE answers (
    id SERIAL PRIMARY KEY,
    content VARCHAR(255) NOT NULL,
    is_correct BOOLEAN NOT NULL,
    question_id INT NOT NULL REFERENCES questions(id)
);