install.packages("arules")
#pacote arules cria as regras para classificação
install.packages("arulesCBA")

library(arules)
library(arulesCBA)

#install.packages("caret", dependencies=T)
library(caret)
library(plotrix)

tabela_music_mental_health <- read.csv('D:\\Codigos_VSCODE\\Programas_didaticos_R\\mxmh_survey_results.csv')

head(tabela_music_mental_health,2)

quem_melhorou <- tabela_music_mental_health[tabela_music_mental_health$Music.effects == 'Improve', ]
quem_piorou <- tabela_music_mental_health[tabela_music_mental_health$Music.effects == 'Worsen', ]
sem_efeito <- tabela_music_mental_health[tabela_music_mental_health$Music.effects == 'No effect', ]

tabelaSemNA<- na.omit(tabela_music_mental_health)

tabelaSemNA <- tabelaSemNA[tabelaSemNA$Music.effects != "" , ] # evitar classe vazia prevista
eliminar_valores_vazios = tabela_music_mental_health[tabela_music_mental_health$Timestamp != "" & 
                                                     tabela_music_mental_health$Age != ""&
                                                     tabela_music_mental_health$Primary.streaming.service != ""&
                                                     tabela_music_mental_health$Hours.per.day != "" &
                                                     tabela_music_mental_health$While.working != "" &
                                                     tabela_music_mental_health$Instrumentalist != "" &
                                                     tabela_music_mental_health$Composer != "" &
                                                     tabela_music_mental_health$Fav.genre != "" &
                                                     tabela_music_mental_health$Exploratory != "" &
                                                     tabela_music_mental_health$Foreign.languages != "" &
                                                     tabela_music_mental_health$BPM != "" &
                                                     tabela_music_mental_health$Frequency..Classical. != "" &
                                                     tabela_music_mental_health$Frequency..Country. != "" &
                                                     tabela_music_mental_health$Frequency..EDM. != "" &
                                                       tabela_music_mental_health$Frequency..Folk. != "" &
                                                       tabela_music_mental_health$Frequency..Gospel. != "" &
                                                       tabela_music_mental_health$Frequency..Hip.hop. != "" &
                                                       tabela_music_mental_health$Frequency..Jazz. != "" &
                                                       tabela_music_mental_health$Frequency..K.pop. != "" &
                                                       tabela_music_mental_health$Frequency..Latin. != "" &
                                                       tabela_music_mental_health$Frequency..Lofi. != "" &
                                                       tabela_music_mental_health$Frequency..Metal. != "" &
                                                       tabela_music_mental_health$Frequency..Pop. != "" &
                                                       tabela_music_mental_health$Frequency..R.B. != "" &
                                                       tabela_music_mental_health$Frequency..Rap. != "" &
                                                       tabela_music_mental_health$Frequency..Rock. != "" &
                                                       tabela_music_mental_health$Frequency..Video.game.music. !="" &
                                                       tabela_music_mental_health$Music.effects != "" &
                                                       tabela_music_mental_health$Permissions !="", ]


tabela_music_mental_health<-tabelaSemNA


#----------tabela para analise e previsao---------------#

tabela_previsao <- subset(tabela_music_mental_health, select = -c(Timestamp, Primary.streaming.service, Permissions))


tabela_music_mental_health$Music.effects = as.factor(tabela_music_mental_health$Music.effects)


modelo = CBA(Music.effects ~ . , tabela_music_mental_health, supp=0.05, conf=0.9)

inspect(modelo$rules)
regras<-modelo$rules

previsao = predict(modelo,tabela_music_mental_health) # sem separar conjunto de dados de treino
head(previsao)
confusionMatrix(previsao, tabela_music_mental_health$Music.effects)

library("arulesViz")

regrasApriori = apriori(tabela_music_mental_health, parameter = 
                          list(supp=0.03, conf=0.4, minlen=2))

summary(regrasApriori)
inspect(regrasApriori)
plot(regras, method="graph")
plot(regras, method="grouped")
plot(regras, method="matrix")



ansiedade = tabela_music_mental_health$Anxiety
ocd = tabela_music_mental_health$OCD
depressao = tabela_music_mental_health$Depression
insonia = tabela_music_mental_health$Insomnia

summary(precos_aptos)
desvio_padrao_apartamentos = sd(precos_aptos)
variancia_apartamentos = var(precos_aptos)
Coef_Var <- function(x){
  sd(x)/mean(x)*100
}


#------ansiedade
summary(ansiedade)
media_ansiedade = mean(ansiedade)
dp_ansiedade = sd(ansiedade)
var_ansiedade = var(ansiedade)
cf_ansiedade = Coef_Var(ansiedade)
media_ansiedade
dp_ansiedade
var_ansiedade



# ------insonia
summary(insonia)
media_insonia = mean(insonia)
dp_insonia = sd(insonia)
var_insonia = var(insonia)
cf_insonia = Coef_Var(insonia)
media_insonia
dp_insonia
var_insonia
cf_insonia

#------ocd
summary(ocd)
media_ocd = mean(ocd)
dp_ocd = sd(ocd)
var_ocd = var(ocd)
cf_ocd = Coef_Var(ocd)
media_ocd
dp_ocd
var_ocd
cf_ocd


#-------Depressao

summary(depressao)
media_depressao = mean(depressao)
dp_depressao = sd(depressao)
var_depressao = var(depressao)
cf_depressao = Coef_Var(depressao)
media_depressao
dp_depressao
var_depressao
cf_depressao