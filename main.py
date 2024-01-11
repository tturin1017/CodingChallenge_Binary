def convert_to_decimal(binary_num):
  dec = 0
  #write your code here
  return dec #return a number 


def convert_to_binary(x):
  string_bin=''
  #write your code here
  return string_bin #return a string for binary sequence



#########DO NOT DELETE OR EDIT THE CODE BELOW ##############################################
def test_answer():
  result = convert_to_decimal(11011)
  assert result == 27
  
def test_answer2():
    assert convert_to_decimal(111111111)==511

def test_answer3():
    assert convert_to_decimal(1011001011011)==5723


def test_answer4():
    assert convert_to_decimal(1000000000)==512

def test_answer5():
    assert convert_to_binary(27)=='11011'

def test_answer6():
    assert convert_to_binary(511)=='111111111'

def test_answer7():
    assert convert_to_binary(5723)=='1011001011011'
