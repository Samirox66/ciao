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