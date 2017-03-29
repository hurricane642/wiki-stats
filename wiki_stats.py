#!/usr/bin/python3

import os
import sys
import math

import array

import statistics

from matplotlib import rc
rc('font', family='Droid Sans', weight='normal', size=14)

import matplotlib.pyplot as plt


class WikiGraph:

    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename)

        with open(filename) as f:
            str=f.read.split=[int(i) for i in (str[0],str[1])]
            (n, _nlinks) = (0, 0)
            
            self._titles = []
            self._sizes = array.array('L', [0]*n)
            self._links = array.array('L', [0]*_nlinks)
            self._redirect = array.array('B', [0]*n)
            self._offset = array.array('L', [0]*(n+1))

            b=3 #создание массива offset
            c=0
            self._offset[0]=0
            for a in range(1,n+1):
                self._offset[b]=self._offset[a-1]+ int(str[b+2])
                self._titles.append(str[b+1])
                self._sizes[c]=int(str[b])
                self._redirect[c]=int(str[b+1])
                c=c+1
                b=b+int(str[b+2])+4
            #создание линкса- массива вершин
            b=5
            a=0
            while a<len(str):
                mas=[int(i) for i in str[b+1:b+1+int(str[b])]]
                for i in mas:
                   self._links[a]=i
                   a=a+1
                b=b+int(str[b])+4
        print('Граф загружен')

    def get_number_of_links_from(self, _id):
        return(len(self.get_links_from(_id)))
    def get_links_from(self, _id):
        return self._links[self._offset[_id]:self._offset[_id+1]]
    def get_id(self, title):
        for i in range(len(self._titles)):
            if title==self._titles[i]:
                return(i)
    def get_number_of_pages(self):
        return len(self._sizes)
    def is_redirect(self, _id):
        if self._redirect[_id]:
            return True
        return False
    def get_title(self, _id):
        return self._titles[_id]
    def get_page_size(self, _id):
        return self._sizes[_id]

def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()
    # TODO: нарисовать гистограмму и сохранить в файл


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Использование: wiki_stats.py <файл с графом статей>')
        sys.exit(-1)

    if os.path.isfile(sys.argv[1]):
        wg = WikiGraph()
        wg.load_from_file(sys.argv[1])
    else:
        print('Файл с графом не найден')
        sys.exit(-1)

    # TODO: статистика и гистограммы
