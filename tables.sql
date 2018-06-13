CREATE TABLE Users(
username varchar(50) NOT NULL primary key,
password varchar(70) NOT NULL,
email varchar(50) NOT NULL UNIQUE,
foreign key(username) references MasterTable(username) on delete cascade on update cascade
);


CREATE Table AmountDues(
username varchar(50) NOT NULL primary key,
units_used INT NOT NULL,
connection_id BIGINT NOT NULL UNIQUE,
due_date DATE,
foreign key(connection_id) references MasterTable(connection_id) on delete cascade on update cascade
);


CREATE TABLE Connections(
connection_id BIGINT NOT NULL UNIQUE PRIMARY KEY,
name varchar(150) NOT NULL,
foreign key(connection_id) references MasterTable(id) on delete cascade on update cascade);

CREATE TABLE CustomerDetails(
id BIGINT NOT NULL UNIQUE,
email varchar(150) NOT NULL primary key,
username varchar(50) NOT NULL UNIQUE,
password varchar(70) NOT NULL,
name varchar(150) NOT NULL,
address varchar(400) NOT NULL,
city ENUM('New Delhi', 'Ahmedabad','Bangalore', 'Mumbai', 'Kolkata') NOT NULL,
foreign key(email) references MasterTable(email) on delete cascade on update cascade
);

CREATE TABLE storeadmins_master(
admin_id BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY UNIQUE,
username varchar(50) NOT NULL UNIQUE,
password varchar(70) NOT NULL);



CREATE TABLE UserComplaints(
username varchar(50) NOT NULL primary key,
complaint_id varchar(100) UNIQUE NOT NULL,
complaint TEXT,
foreign key(username) references MasterTable(username) on delete cascade on update cascade);



CREATE TABLE MasterTable(
id BIGINT NOT NULL primary key,
username varchar(50) NOT NULL UNIQUE,
password varchar(70) NOT NULL,
email varchar(150) NOT NULL UNIQUE,
name varchar(150) NOT NULL,
address varchar(400) NOT NULL,
city ENUM('New Delhi', 'Ahmedabad','Bangalore', 'Mumbai', 'Kolkata') NOT NULL,
connection_id BIGINT UNIQUE
);





/*CREATE TABLE CustomerBills(
bill_id BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY UNIQUE,
name varchar(100) NOT NULL,
username varchar(30) UNIQUE NOT NULL,
payable_amount INT NOT NULL,
foreign key(bill_id) references MasterTable(bill_id) on delete cascade on update cascade);
*/