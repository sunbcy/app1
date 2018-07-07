# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
import scrapy
import os

class ImagePipeline(ImagesPipeline):
    # def process_item(self,item,spider):
    IMAGE_STORE = get_project_settings().get("IMAGE_STORE")

    def get_media_requests(self, item, info):
        url = item["imageLink"]
        yield scrapy.Request(url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        os.rename(self.IMAGE_STORE+"/" +image_paths[0],self.IMAGE_STORE+"/"+item['name']+".jpg")
        item["imagePath"] = self.IMAGE_STORE + "/" + item["name"] + ".jpg"
        return item
        # if not image_paths:
        #     raise DropItem("Item contains no images")
        # return item



#
# class App1Pipeline(object):
#     def __init__(self):
#         self.filename = open("hero.csv", "wb+")
#
#     def process_item(self, item, spider):
#         csv_text = str(item["id"]) + "," + str(item["name"]) + "," + str(
#             item["imageLink"]) +"\n"
#         self.filename.write(csv_text.encode("utf-8"))
#
#     def close(self, spider):
#         self.filename.close()
