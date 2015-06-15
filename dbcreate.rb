# -*- coding: utf-8 -*-

require 'rubygems'
require 'sqlite3'

db = SQLite3::Database.new("location.db")
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

db.execute('select * from Location') do |row|
  puts row.join("\t")
end
db.close

