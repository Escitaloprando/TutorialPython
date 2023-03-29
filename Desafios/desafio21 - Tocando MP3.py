#Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.
import vlc
p = vlc.MediaPlayer("hino-gremio-rs.mp3")
p.play()