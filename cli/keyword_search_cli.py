#!/usr/bin/env python3
import json

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            print(f"Searching for: {args.query}")
            
        case _:
            parser.print_help()
    
    
    
    result = []
    data = {}        
    with open("data/movies.json", "r") as file:
        data = json.load(file)
    for movie in data["movies"]:
        if args.query.lower() in movie["title"].lower():
            result.append(movie)

    for i, movie in enumerate(result):
        print(f"{i+1}. Movie Title {movie["title"]}")


if __name__ == "__main__":
    main()