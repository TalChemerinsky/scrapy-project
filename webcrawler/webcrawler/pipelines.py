import csv

class WebcrawlerPipeline:
    def open_spider(self, spider):
        self.file = open('bookdata.csv', 'w', newline='')
        self.writer = csv.DictWriter(self.file, fieldnames=['Name', 'Link', 'Price', 'Category', 'Rating', 'Availability'])
        self.writer.writeheader()

    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item

    def close_spider(self, spider):
        self.file.close()

