# Иерархия исключений и перехват всех ошибок


try:
    first_num = int(input("Please enter a number: "))
    second_num = int(input("Please enter another number: "))

    result = first_num/second_num
except (ValueError,ZeroDivisionError)  as e: # Множественное исключение в кортеже   # Конкретные ошибки вперед
    print(e)
    pass
except Exception as e:                                                              # все ошибки потом
    print(e)
    pass
else:
    print(result)
finally:
    print('Program Ending')




def get_item(data, key):
    """Получить элемент из списка или словаря по ключу/индексу."""
    try:
        return data[key]
    except (IndexError, KeyError) as e:
        print(f"❌ Элемент не найден: {e}")
        return None
    except TypeError as e:
        print(f"❌ Неверный тип ключа: {e}")
        return None
    except Exception as e:
        # Ловим всё остальное — на случай, если data не список и не dict
        print(f"⚠️ Неожиданная ошибка ({type(e).__name__}): {e}")
        return None
# Тесты
print(get_item([1, 2, 3], 10))        # IndexError
print(get_item({"a": 1}, "b"))        # KeyError
print(get_item([1, 2, 3], "abc"))     # TypeError
print(get_item(None, 0))              # TypeError (None не subscriptable)
print(get_item({'name':'Vadim'}, 'surname'))
