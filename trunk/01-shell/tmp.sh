#!/bin/bash
function AA
{
read -p "Please input a number:" NUMBER
}
function BB
{
if [ $NUMBER == a ];then
	echo "your input is a"
	else
	echo "what's your input?"
fi
}
AA
BB
