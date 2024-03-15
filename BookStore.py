import Book
import ArrayList
import ArrayQueue
import RandomQueue
import DLList
import SLLQueue
import MaxQueue
import ChainedHashTable
import time
import BinarySearchTree
import BinaryHeap
##import AdjacencyList


class BookStore:
  def __init__(self):
    self.bookCatalog = None
    #self.shoppingCart = ArrayQueue.ArrayQueue()
    self.shoppingCart = MaxQueue.MaxQueue()
    #self.bookIndices = ChainedHashTable.ChainedHashTable() 
    self.sortedTitleIndices = BinarySearchTree.BinarySearchTree()

  def loadCatalog(self, fileName: str):
    self.bookCatalog = ArrayList.ArrayList()
    with open(fileName, encoding="utf8") as f:
      # The following line is the time that the computation starts
      start_time = time.time()
      for line in f:
        (key, title, group, rank, similar) = line.split("^")
        b = Book.Book(key, title, group, rank, similar)
        self.bookCatalog.append(b)
        ##self.bookIndices.add(key, self.bookCatalog.size()-1)
        self.sortedTitleIndices.add(title, self.bookCatalog.size() - 1)
      # The following line is used to calculate the total time of execution
      elapsed_time = time.time() - start_time
      print(
        f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

  def setRandomShoppingCart(self):
    q = self.shoppingCart
    start_time = time.time()
    #self.shoppingCart = RandomQueue.RandomQueue()
    while q.size() > 0:
      self.shoppingCart.add(q.remove())
    elapsed_time = time.time() - start_time
    print(f"Setting radomShoppingCart in {elapsed_time} seconds")

  def setShoppingCart(self):
    q = self.shoppingCart
    start_time = time.time()
    self.shoppingCart = ArrayQueue.ArrayQueue()
    while q.size() > 0:
      self.shoppingCart.add(q.remove())
    elapsed_time = time.time() - start_time
    print(f"Setting radomShoppingCart in {elapsed_time} seconds")

  def removeFromCatalog(self, i: int):
    # The following line is the time that the computation starts
    start_time = time.time()
    self.bookCatalog.remove(i)
    # The following line is used to calculate the total time
    # of execution
    elapsed_time = time.time() - start_time
    print(f"Remove book {i} from books in {elapsed_time} seconds")

  def addBookByIndex(self, i: int):
    # Validating the index. Otherwise it  crashes
    if i >= 0 and i < self.bookCatalog.size():
      start_time = time.time()
      s = self.bookCatalog.get(i)
      added = self.shoppingCart.add(s)
      elapsed_time = time.time() - start_time
      if type(added) == bool and added:
        print(f"Added to shopping cart {s} \n{elapsed_time} seconds")
      else:
        print(
          f"Attempted to add {s} to shopping cart.\nAddition was not confirmed."
        )

  def searchBookByInfix(self, infix: str, cnt: int):
    '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string    
        '''
    start_time = time.time()
    count = 0
    for index in self.bookCatalog: #searches for book
      if infix in index.title: #searches for infix in tittles
        print(index) #prints tittles
        count += 1
      if cnt == count: ##breaks once it printed "cnt" times
        break
    # todo
    elapsed_time = time.time() - start_time
    print(f"searchBookByInfix Completed in {elapsed_time} seconds")

  def removeFromShoppingCart(self):
    start_time = time.time()
    if self.shoppingCart.size() > 0:
      u = self.shoppingCart.remove()
      elapsed_time = time.time() - start_time
      print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")

  def getCartBestSeller(self):
    start_time = time.time()
    x = self.shoppingCart.max()
    elapsed_time = time.time() - start_time
    print(f"getCartBestSeller returned\n{x.title}\nCompleted in {elapsed_time} seconds")

  def addBookByKey(self, key):
    start_time = time.time()
    i = self.bookIndices.find(key)
    if i != None:
      b = self.bookCatalog.get(i)
      self.shoppingCart.add(b)
      print(f'Added title: {b.title}')
    else:
      print('Book not found.')
    elapsed_time = time.time() - start_time
    print(f"addBookByKey Completed in {elapsed_time} seconds")

  def addBookByPrefix(self, prefix):
    start_time = time.time()
    t = self.sortedTitleIndices.smallest_key(prefix)
    b = self.bookCatalog.get(t)
    if b.title[0:len(prefix)] == prefix and prefix != '':
        self.shoppingCart.add(b)
        print(f"Added first matched title: {b.title}")
    else:
        print("Prefix was not found.")
    elapsed_time = time.time() - start_time
    print(f"addBookByPrefix Completed in {elapsed_time} seconds")

  def bestsellers_with(self, infix, structure, n = 0) :
      best_sellers = None
      if structure == 1:
          best_sellers = BinarySearchTree.BinarySearchTree()
      elif structure == 2:
          best_sellers = BinaryHeap.BinaryHeap()
      else:
          print("Invalid data structure.")
      if best_sellers is not None:
          if infix == "":
              print("Invalid infix.")
          else:
              start_time = time.time()
              #FIXME: Insert the rest of the implementation here
              if structure == 1: ##highest rank
                  c = 0
                  for book in self.bookCatalog:
                      if infix in book.title:
                          best_sellers.add(book.rank, book)
                          c += 1
                          if c >= n:
                              break
                  for i in range(best_sellers.size()):
                      for book in self.bookCatalog:
                          if best_sellers.find(book.rank) != None:
                              print(book)
              else: ##lowest rank
                  c = 0
                  for book in self.bookCatalog:
                      if infix in book.title:
                          best_sellers.add((book.rank * -1))
                          c += 1
                      if c >= n:
                          break
                  for i in range(best_sellers.n):
                      for book in self.bookCatalog:
                          if best_sellers.a[i] * -1 == book.rank:
                              print(book)
              elapsed_time = time.time() - start_time
              print(f"Displayed bestsellers_with({infix}, {structure}, {n}) in {elapsed_time} seconds")

