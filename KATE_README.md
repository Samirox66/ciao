Работаем с файлами:
dsl_info.py
ciao/*gv
ciao.sgi
example (current - flip-flop)

комменты:
virt.py


ciao.json содержит пути к папкам, в которых прописаны обхекты диаграммы - файлы .gv


! все что в dsl_info должно соответствовать .gv и примеру !


ПЛАН:
var.gv - ok
state.gv - ok
TRANSITION_DESCRIPTION - строчка, которая описывает переход в наших состояниях (state -> // -> state). Используем ее в state_block
TRANSITION_DESCRIPTION  - пееписать в соответствии с грамматикой!
вопрос: в файле TRANSITION_DESCRIPTION мы разделяем стрелки и имена на до и после. надо ли так?

ОЧЕНЬ ВАЖНО: ВСЕГДА ПРОПИСЫВАТЬ EVENT! СОСТОЯНИЯ УСТОЙЧИВЫЕ, ПРОСТО ТАК НЕ ПЕРЕХОДЯТ, ИНАЧЕ КОД ПАДАЕТ. (ОШИБКА НЕ НАХОДИТ <НАЗВАНИЕ ПРОГРАММЫ> УКАЗЫВАЕТ НА ТО, ЧТО НЕВЕРНО ПРОПИСАН ПРИМЕР) ну или недочет в грамматике перехода

ОЧЕНЬ ВАЖНО: числа в VAR указывать только с дробной частью!


TODO:
1. вынести начальное состояние
2. Подумать про variables
3. Эффект может быть выражением -> встроить это выражение в грамматику 
tokens которые могут быть expr:      + = return true false var int ; .
4. 

1. производитель - потребиель
2. лифт - пассажир
3. философ - вилка