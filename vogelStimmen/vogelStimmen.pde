String[] items = {
  "ALPENKRÄHE",
  "DÜNNSCHNABEL-BRACHVOGEL",
  "EINFARBDROSSEL",
  "EINSIEDLERDROSSEL",
  "GRAUORTOLAN",
  "GRAUWANGENDROSSEL",
  "GRÜNWALDSÄNGER",
  "KATZENVOGEL",
  "KRONENLAUBSÄNGER",
  "NODDISEESCHWALBE",
  "PAZIFIKPIEPER",
  "PHARAONENZIEGENMELKER",
  "PRÄRIELÄUFER",
  "ROTKEHLDROSSEL",
  "ROTSCHWANZDROSSEL",
  "SANDFLUGHUHN",
  "SCHMUCKREIHER",
  "STEINSPERLING",
  "STREIFENSCHWIRL",
  "STUMMELLERCHE",
  "TÜRCKENAMMER",
  "WACHOLDERLAUBSÄNGER",
  "WEISSFLÜGELLERCHE",
  "WERMUTREGENPFEIFER",
  "ZWERGDROSSEL"
};
PFont customFont;
int itemLength = 25;
int currentIndex = 13;

void setup() {
  size(1080, 720, P3D);

  customFont = createFont("synchro.ttf", 32);
  textFont(customFont, 80);
}
void draw() {
  background(0);
  beginShape();
  fill(#FF36FC);
  vertex(0, 0);
  vertex(width, 0);
  fill(#1E2AF7);
  vertex(width, height);
  vertex(0, height);
  endShape();


  textAlign(LEFT);
  fill(#EEA8FC);
  noStroke();
  rectMode(CORNER);

  rect(0, height/2+25, width, -72);
  int text_size = 40;
  textSize(40);
  fill(255);
  text(items[currentIndex], width*0.18, height/2);

  float margin = (height/12);

  //up

  for (int s=1; s<6; s++) {

    String shown = "";
    if (currentIndex-s < 0) {
      shown = items[itemLength+(currentIndex-s)];
    } else {
      shown = items[currentIndex-s];
    }
    fill(#EEA8FC, 255 - (s*15));
    textSize(text_size - s*2);

    text(shown,
      width*0.18 - s*30, height/2 - s * margin);
  }
  for (int s=1; s<6; s++) {
    String shown = "";
    if (currentIndex+s >= itemLength) {
      shown = items[(currentIndex+s)-itemLength];
    } else {
      shown = items[currentIndex+s];
    }
    textSize(text_size- s*2);

    fill(#EEA8FC, 255 - (s*15));
    text(shown,
      width*0.18 - s*30, height/2 + s * margin);
  }
}
void keyReleased() {
  if (keyCode == UP) {
    currentIndex = (currentIndex - 1 + itemLength) % itemLength;
  } else if (keyCode == DOWN) {
    currentIndex = (currentIndex + 1) % itemLength;
  }
  if (key == ENTER) {
    // Handle ENTER key release here, e.g., perform an action on the selected item
    println("Selected Item: " + items[currentIndex]);
  }
}
