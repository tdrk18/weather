# -*- coding: utf-8 -*-

require 'rubygems'
require 'sqlite3'

unless File.exists?("config") then
  `mkdir config`
end

unless File.exists?("config/location.db") then
  db = SQLite3::Database.new("config/location.db")
  sql = <<SQL
create table Location (
name varchar(10),
num  integer
);
SQL
  db.execute(sql)

  db.transaction do
    sql = "insert into Location values (?, ?)"
    File.open("data.txt").each_line do |line|
      line = line.split(",")
      db.execute(sql, line[0], line[1].chomp.to_i)
    end
  end
  db.close
end

db = SQLite3::Database.open("config/location.db")
name = "a"
id = 0
db.execute("select * from Location where name=\"#{name}\"") do |row|
  id = row[1]
end
db.close

if id == 0 then
  puts "Sorry, #{name} does not exist in DATABASE."
else
  puts "id: #{id}"
end

