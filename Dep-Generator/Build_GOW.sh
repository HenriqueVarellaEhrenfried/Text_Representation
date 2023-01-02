echo "Create Outupuy directory..."

mkdir -p ../Datasets/MR/MR-GOW-TAG-None
mkdir -p ../Datasets/Ohsumed/Ohsumed-GOW-TAG-None

mkdir -p ../Datasets/B2W/B2W_COMPLETE-Rating-GOW-TAG-None
mkdir -p ../Datasets/10kGNAD-DE/10kGNAD-GOW-TAG-None

echo "Build datasets..."

# English Dataset
python main.py -i ../Datasets/MR/Parsed/ -o ../Datasets/MR/MR-GOW-TAG-None -n MR -s Train -d 300 -c 20 -l en -g gow -t none;
python main.py -i ../Datasets/Ohsumed/Output-dataset/ -o ../Datasets/Ohsumed/Ohsumed-GOW-TAG-None -n Ohsumed -s Train -d 300 -c 20 -l en -g gow -t none;

# Portuguese Dataset
python main.py -i ../Datasets/B2W-PT/Raw/B2W-Rating-Balanced/ -o ../Datasets/B2W/B2W_COMPLETE-Rating-GOW-TAG-None -n B2W-Rating -s Train -d 300 -c 20 -l pt -g gow -t none;

# German Dataset
python main.py -i ../Datasets/10kGNAD-DE/Parsed/ -o ../Datasets/10kGNAD-DE/10kGNAD-GOW-TAG-None -n 10kGNAD-DE -s Train -d 300 -c 20 -l de -g gow -t none;


echo "Renaming Files..."

mv ../Datasets/MR/MR-GOW-TAG-None/Train_MR.txt      ../Datasets/MR/MR-GOW-TAG-None/MR-GOW-TAG-None.txt 
mv ../Datasets/Ohsumed/Ohsumed-GOW-TAG-None/Train_Ohsumed.txt ../Datasets/Ohsumed/Ohsumed-GOW-TAG-None/Ohsumed-GOW-TAG-None.txt
mv ../Datasets/B2W/B2W_COMPLETE-Rating-GOW-TAG-None/Train_B2W-Rating.csv ../Datasets/B2W/B2W_COMPLETE-Rating-GOW-TAG-None/B2W_COMPLETE-Rating-GOW-TAG-None.txt
mv ../Datasets/10kGNAD-DE/10kGNAD-GOW-TAG-None/Train_10kGNAD-DE.txt ../Datasets/10kGNAD-DE/10kGNAD-GOW-TAG-None/10kGNAD-GOW-TAG-None.txt

