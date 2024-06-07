-- Création de la table contrats
CREATE TABLE t_contrats (
    ID_Contrat INT AUTO_INCREMENT PRIMARY KEY,
    ID_Artiste INT,
    Date_Contrat DATE,
    Description_Contrat TEXT,
    Montant DECIMAL(10,2),
    FOREIGN KEY (ID_Artiste) REFERENCES t_artistes(ID_Artiste)
);

-- Création de la table artistes
CREATE TABLE t_artistes (
    ID_Artiste INT AUTO_INCREMENT PRIMARY KEY,
    Nom_Artiste VARCHAR(100),
    Prenom_Artiste VARCHAR(100)
);

-- Insérer un contrat
INSERT INTO t_contrats (ID_Artiste, Date_Contrat, Description_Contrat, Montant) VALUES (1, '2024-01-01', 'Description du contrat', 1000.00);

-- Mettre à jour un contrat
UPDATE t_contrats SET Date_Contrat='2024-02-01', Description_Contrat='Nouvelle description', Montant=2000.00 WHERE ID_Contrat=1;

-- Supprimer un contrat
DELETE FROM t_contrats WHERE ID_Contrat=1;

-- Sélectionner tous les contrats
SELECT * FROM t_contrats;
