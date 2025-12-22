# Εργασία Git – Collaborative Workflow : “The Python Cookbook”

## Οδηγίες για φοιτητές

### Στόχος εργασίας
Τις επόμενες δύο εβδομάδες, η ομάδα σας θα συνεργαστεί χρησιμοποιώντας Git και GitHub. Ο στόχος είναι να εξασκηθείτε στο Git, όχι στην προγραμματιστική γλώσσα. Θα εξασκηθείτε σε ένα ρεαλιστικό Git workflow, όπου πολλά άτομα δουλεύουν πάνω στο ίδιο project.

Θα μάθετε να:
    • κάνετε clone από GitHub
    • δουλεύετε σε δικό σας branch
    • κάνετε commits
    • στέλνετε την δουλειά σας στο GitHub (push)
    • ανοίγετε Pull Request
    • επιλύετε merge conflicts
    • συγχωνεύετε (merge) τις αλλαγές σας στο master 
    • Συγχρονισμός και καθάρισμα branches
Η εργασία είναι ατομική, αλλά το repository είναι κοινό.

---

### Μέρος 1 – Clone του repository
    1. Συνδεθείτε στο GitHub και ανοίξτε το repository της ομάδας σας.
    2. Επιλέξτε Code και αντιγράψτε το HTTPS URL.
    3. Ανοίξτε Terminal / Git Bash.
    4. Μεταβείτε στον φάκελο που θέλετε να αποθηκευτεί το project (π.χ. Documents, Dev).
    5. Εκτελέστε την εντολή clone που μάθαμε στο μάθημα, χρησιμοποιώντας το URL.
(Δεν την γράφω εδώ επίτηδες – πρέπει να τη θυμηθείτε από τις σημειώσεις σας.)
Αν όλα πήγαν σωστά, θα εμφανιστεί νέος φάκελος με το όνομα του project.

---

### Μέρος 2 – Προετοιμασία του master branch
    1. Από το Terminal μπείτε στον φάκελο του project.
    2. Βεβαιωθείτε ότι βρίσκεστε στο master branch.
    3. Ενημερώστε το master ώστε να είναι ίδιο με το GitHub (pull από το remote).
Στόχος: να ξεκινήσετε από την πιο πρόσφατη έκδοση του κώδικα.

---

### Μέρος 3 – Δημιουργία προσωπικού branch
Κάθε φοιτητής δουλεύει στο δικό του branch ώστε να μην επηρεάζει απευθείας το master.
    1. Δημιουργήστε νέο branch και ταυτόχρονα μεταβείτε σε αυτό με όνομα:
recipe-<το_όνομά_σας>
Παράδειγμα:
recipe-christos
    2. Ελέγξτε ότι όντως βρίσκεστε στο νέο branch (με την εντολή που εμφανίζει όλα τα branches).

---

### Μέρος 4 – Προσωπική συνταγή (Commit 1)
    1. Μέσα στο φάκελο recipes/ δημιουργήστε ένα νέο αρχείο Python με το όνομά σας, π.χ.:
recipes/christos_recipe.py
    2. Γράψτε απλό placeholder content, π.χ.:
def recipe():
    return "Boil pasta and add sauce."
    3. Προσθέστε το νέο αρχείο στο staging area (add).
    4. Κάντε commit με μήνυμα:
Add personal recipe

---

### Μέρος 5 – Τροποποίηση shared αρχείου (Commit 2)
Όλοι θα αλλάξουν το ίδιο αρχείο => πιθανά merge conflicts.
    1. Ανοίξτε το αρχείο:
main.py
    2. Εντοπίστε τη λίστα, π.χ.:
recipes = [
   // Add your name here
]
    3. Προσθέστε το όνομά σας, π.χ.:
recipes = [
   "Christos",
]
    4. Αποθηκεύστε.
    5. Προσθέστε την αλλαγή στο staging area.
    6. Κάντε commit με μήνυμα:
Add name to shared list

---

### Μέρος 6 – Push του branch στο GitHub
    1. Επιβεβαιώστε ότι είστε στο branch σας (recipe-<name>).
    2. Στείλτε (push) το branch στο origin remote.
    3. Αν ζητηθεί, ορίστε tracking ώστε να γίνει upstream association.
Μετά από αυτό, το branch θα εμφανιστεί στο GitHub.

---

### Μέρος 7 – Pull Request (PR)
Στο GitHub:
    1. Ανοίξτε το repository.
    2. Κανονικά θα δείτε προτροπή “Compare & pull request”.
Αν όχι, δημιουργήστε PR χειροκίνητα:
    • Base: master
    • Compare: recipe-<yourname>
    3. Ορίστε τίτλο:
Add recipe + name
    4. Γράψτε σύντομη περιγραφή (2–3 προτάσεις).
    5. Δημιουργήστε το Pull Request.

---

### Μέρος 8 – Merge conflicts (αν υπάρξουν)
Αν το GitHub αναφέρει ότι το PR έχει conflicts:
    1. Τοπικά στον υπολογιστή:
        ◦ Μεταβείτε στο master
        ◦ Κάντε pull από το remote
    2. Στη συνέχεια επιστρέψτε στο branch σας (recipe-<name>).
    3. Συγχωνεύστε master → branch.
    4. Το Git θα εμφανίσει conflict markers π.χ.:
<<<<<<< HEAD
"Christos"
=======
"Maria"
>>>>>>> master
    5. Τροποποιήστε το αρχείο ώστε να διατηρηθούν και οι δύο εγγραφές, π.χ.:
recipes = [
   "Christos",
   "Maria",
]
    6. Αποθηκεύστε.
    7. Προσθέστε την επίλυση στο staging.
    8. Κάντε commit με μήνυμα:
Resolve merge conflict in main.py
    9. Push ξανά το branch.
Μετά από αυτό, το PR θα μπορεί να γίνει merge.

Μέρος 9 – Merge του PR & cleanup
Αφού γίνει merge το PR στο GitHub:
    1. Τοπικά:
        ◦ Μεταβείτε στο master
        ◦ Κάντε pull για συγχρονισμό
    2. Προαιρετικά αλλά συνιστάται:
        ◦ Διαγράψτε το branch σας τοπικά ώστε να καθαρίσει το project.

---

### Τι θα παραδώσετε
Για την αξιολόγηση κάθε φοιτητής θα στείλει:
    1. Link στο Pull Request.
    2. Screenshot από conflict στο αρχείο (πριν/κατά την επίλυση).
    3. Screenshot από commit history του branch (π.χ. git log --oneline ή από GitHub UI).
    4. Μικρό κείμενο 3–5 προτάσεων με τίτλο:
       Τι έμαθα, τι με δυσκόλεψε, και τι μου άρεσε από το branch workflow και τα conflicts, και γενικά δουλεύωντας με το git και το Github.

---

## Κριτήρια αξιολόγησης (σύνολο 20 βαθμοί)
| Κατηγορία | Βαθμοί |
|---|---|
| Σωστά Branch + commits | 10 
| Pull Request created properly | 4
| Conflict resolution | 4
| Hygiene (merge cleanup) | 2

--- 

### *Reminder!

Μην κάνετε αλλαγές απευθείας στο `master` branch.
Χρησιμοποιήστε μόνο personal feature branches.
