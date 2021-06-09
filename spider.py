import os
import argparse

import scrapy
 
 
class ScraPictureItem(scrapy.Item):
 
    pic_url = scrapy.Field()















if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--url",default="", type=str,required=False, help="Give a url to be as the start point")