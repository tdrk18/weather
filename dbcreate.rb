# -*- coding: utf-8 -*-

require 'rubygems'
require 'sqlite3'

def dbcreate()
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
      File.open("data/location.csv").each_line do |line|
        line = line.split(",")
        db.execute(sql, line[0], line[1].chomp.to_i)
      end
    end
    db.close
  end
end

def getCityID(name)
  db = SQLite3::Database.open("config/location.db")
  # name = "仙台"
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
  id
end

if __FILE__ == $0 then
  if ARGV.length == 0 then
    puts "Please input the city-name."
    exit 1
  end
  name = ARGV[0]
  dbcreate()
  getCityID(name)
end

