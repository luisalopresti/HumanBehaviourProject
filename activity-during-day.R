library(ggplot2)

# load data
setwd("C:/Users/luisa/Desktop/HumanBehaviour_PRJ/")
df <- read.csv(file="act.csv") 
# file obtained from the chart-act-by-day notebook, 
# after re-encoding activities into homogeneous categories

df <- subset(df, select = -c(where, with_who, mood, X, day))
df <- na.omit(df)
act <- unique(df$what)
act
df<-df[!(df$what == 'Expired'),]


# extract hours
for (t in as.character(df$timestamp)){
  df$hour[startsWith(as.character(df$timestamp), 
                     substr(as.character(df$timestamp), start = 1, stop = 9))] <- 
    substr(as.character(df$timestamp), start = 9, stop = 12)
}

df$hour <- round(as.numeric(df$hour)/100, 0)


# divide in two plots
df1<-df[!(df$what=="Breaks" | df$what=="Eating" | df$what == 'Free time/hobbies' | df$what == 'Others' | df$what == 'Physical activities'),]
df2<-df[(df$what=="Breaks" | df$what=="Eating" | df$what == 'Free time/hobbies' | df$what == 'Others' | df$what == 'Physical activities'),]


ggplot(data=df1) +
  geom_density(aes(x=hour, group=what, fill=what), 
               alpha=0.5, adjust=2) +
  facet_grid(~what, scales = "free_x") +
  labs(title="Activities during the day", 
       y="", x="Hours") +
  scale_y_continuous(labels = c(), breaks = c()) +
  theme_bw()

ggplot(data=df2) +
  geom_density(aes(x=hour, group=what, fill=what), 
               alpha=0.5, adjust=2) +
  facet_grid(~what, scales = "free_x") +
  labs(title="Activities during the day", 
       y="", x="Hours") +
  scale_y_continuous(labels = c(), breaks = c()) +
  theme_bw()

