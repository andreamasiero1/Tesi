#!/bin/bash

echo "----------------------------------------"
echo "Inizio compilazione tesi..."
echo "----------------------------------------"

# 1. Prima compilazione per generare i file ausiliari (.aux, .glo, .bcf)
echo "=> Esecuzione pdflatex (Passo 1/4)"
pdflatex -shell-escape -interaction=nonstopmode tesi.tex > /dev/null

# 2. Generazione bibliografia
echo "=> Esecuzione biber (Passo 2/4)"
biber tesi > /dev/null

# 3. Generazione glossario e acronimi
echo "=> Esecuzione makeglossaries (Passo 3/4)"
makeglossaries tesi > /dev/null

# 4. Ricompilazioni finali per sistemare i riferimenti incrociati
echo "=> Esecuzione pdflatex (Passo 4/4)"
pdflatex -shell-escape -interaction=nonstopmode tesi.tex > /dev/null
pdflatex -shell-escape -interaction=nonstopmode tesi.tex > /dev/null

echo "----------------------------------------"
echo "Compilazione completata! Apertura file..."
echo "----------------------------------------"
open tesi.pdf
