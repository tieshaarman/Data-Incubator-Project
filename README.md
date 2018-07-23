# Data-Incubator-Project

## Bias of the Media: a case study of media representation of terrorism

Terrorism has always played a prominent role of the media and even more so post 9-11. The question is, does the media give us a realistic image of terrorism? The amount of media coverage might not be representative of the actual amount of incidents or victims and might be used to sway public opinion, for instance in favor of support for military actions, while other conflicts might be ignored. In the project I aim to investigate the underlying reasons for a media bias, for instance by looking at correlations with military involvement in certain conflicts or economic relations with the country in question. In a later stage I will also compare different media sources to determine if certain media suppliers are more biased than others.
To investigate the viability of this project I have analyzed two datasets. The first is the Global Terrorism Database, which lists 170,000 terroristic acts recorded from 1970 to 2016. The second is an archive of Reuters news item titles, which was scraped from the Reuters archives by philipperemy and made available on GitHub and contains 8.4 million news titles and timestamps from 2007-2016.

As an example of the spread and intensity of terrorism I have plotted the number of victims of terroristic actions, both wounded and killed, over the period 2013-2016, on the world map using a logarithmic scale. While some observations are obvious like the hotspots in Syria and Iraq, others might be more surprising, like the large number of deaths in Thailand and the Philippines.
To show the correlation between the number of victims and the media coverage I have plotted a bar graph showing the number of victims (divided by 10) in certain countries and the number of article titles containing references to terroristic actions in these countries. The countries are the 15 countries containing the highest number of terrorism victims and a couple of Western-world countries I expected might be over represented like: US, UK, Israel, France and Germany.
The articles were scanned for mentioning the country name in combination with the mentioning of a set of terrorism related terms and well-known terrorist groups: ('terror', 'bomb', 'extremist', 'taliban', 'hamas', 'boko haram', 'isis', 'isil', 'islamic state', 'al qaeda', 'al qaida').

From the graph we see for instance that Syria gets much more media coverage than Iraq or Afghanistan even though the number of terrorism victims is significantly lower. The graph is zoomed to show more details, which actually truncates the Iraq bar at 30,000 but Iraq actually has around 85,000 terrorism victims during the period 2013-2016. One reason for over representation of Syria might be our current military involvement in Syria. To prove such a correlation I will for instance correlate media coverage over time during the periods of active involvement in Afghanistan and Iraq for comparison.
Not surprisingly Western countries are indeed over represented. But with Reuters being a Western news agency this is not surprising. 

Other countries are almost completely ignored, most notably, Somalia. The reasons for the lack of coverage here might be varied: no military involvement, low economic interest, too dangerous for journalist? A more detailed analysis of country statistics like economy, and resources will certainly shed light on this.
 
 ## Original datasets:
 https://www.start.umd.edu/gtd/
 
 https://github.com/philipperemy/Reuters-full-data-set

