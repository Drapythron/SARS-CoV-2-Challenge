#![allow(non_snake_case)]
use simple_matrix::Matrix;
use std::cmp;
use std::convert::TryInto;

fn main() {
    let mut _seq1 = String::from("GTCCCTTAA");
    let _seq2 = String::from("GATTGGAACTGA");

    let alig: Vec<String> = new_entry(_seq1, _seq2);

    println!("El alineamiento es:");
    println!("{}", alig[0]);
    println!("{}", alig[1]);

    let score = getScore(alig, 1, -1, -1);

    println!("La puntuación del alineamiento es: {}", score);
}
fn new_entry(mut _seq1: String, mut _seq2: String) -> Vec<String> {
    _seq1 = str::replace(&_seq1, "N", "A");
    _seq1 = str::replace(&_seq1, "K", "G");

    _seq2 = str::replace(&_seq2, "N", "A");
    _seq2 = str::replace(&_seq2, "K", "G");

    //Convertimos el string en un vector

    let seq1_vec: Vec<char> = _seq1.chars().collect();
    let seq12_vec: Vec<char> = seq1_vec.clone();
    let seq2_vec: Vec<char> = _seq2.chars().collect();
    let seq22_vec: Vec<char> = seq2_vec.clone();

    let row_size = seq1_vec.len() + 1;
    let col_size = seq2_vec.len() + 1;

    let mut _mat: Matrix<i32> = Matrix::new(row_size, col_size);

    _mat = inicialize_matrix(seq1_vec, seq2_vec, 1, -1, -1);

    let alignment: Vec<String> = alignment(seq12_vec, seq22_vec, 1, -1, -1, _mat);

    alignment
}

fn inicialize_matrix(
    _seq1: Vec<char>,
    _seq2: Vec<char>,
    _mach: i32,
    _gap: i32,
    _mismatch: i32,
) -> Matrix<i32> {
    //Creamos la matriz
    let row_size = _seq1.len() + 1;
    let col_size = _seq2.len() + 1;
    let mut _mat: Matrix<i32> = Matrix::new(row_size, col_size);

    //Inicializamos la matriz
    let mut pos = 0;
    for i in 0..row_size {
        let score = pos * _gap;
        _mat.set(i, 0, score);
        pos += 1;
    }

    pos = 0;
    for j in 0..col_size {
        let score = pos * _gap;
        _mat.set(0, j, score.try_into().unwrap());
        pos += 1;
    }
    //Creamos la matriz con los pesos

    for i in 1..row_size {
        for j in 1..col_size {
            //Opción 1 - Miramos la puntuación con la diagonal
            let _nuc1 = _seq1[i - 1];
            let _nuc2 = _seq2[j - 1];
            let opcion1;

            if _nuc1 == _nuc2 {
                opcion1 = _mat.get(i - 1, j - 1).unwrap() + _mach;
            } else {
                opcion1 = _mat.get(i - 1, j - 1).unwrap() + _mismatch;
            }

            //Opción 2 - Miramos la puntuación con la de arriba
            let opcion2 = _mat.get(i - 1, j).unwrap() + _mismatch;

            //Opción 3 - Miramos la puntuación con la izquierda
            let opcion3 = _mat.get(i, j - 1).unwrap() + _mismatch;

            //Escogemos y guardamos el valor máximo de las tres opciones
            let mut max = cmp::max(opcion1, opcion2);
            max = cmp::max(max, opcion3);
            _mat.set(i, j, max);
        }
    }

    _mat
}

fn alignment(
    _seq1: Vec<char>,
    _seq2: Vec<char>,
    _mach: i32,
    _gap: i32,
    _mismatch: i32,
    _mat: Matrix<i32>,
) -> Vec<String> {
    let mut _alignment1: Vec<char> = Vec::new();
    let mut _alignment2: Vec<char> = Vec::new();

    let mut i = _seq1.len();
    let mut j = _seq2.len();

    while i > 0 && j > 0 {
        let score = _mat.get(i, j).unwrap();
        let score_diag = _mat.get(i - 1, j - 1).unwrap();
        let score_up = _mat.get(i - 1, j).unwrap();
        let score_left = _mat.get(i, j - 1).unwrap();

        let score_nuc;
        let _nuc1 = _seq1[i - 1];
        let _nuc2 = _seq2[j - 1];
        if _nuc1 == _nuc2 {
            score_nuc = _mach;
        } else {
            score_nuc = _mismatch;
        }

        if score.eq(&(score_diag + score_nuc)) {
            _alignment1.push(_nuc1);
            _alignment2.push(_nuc2);
            i -= 1;
            j -= 1;
        } else if score.eq(&(score_left + _gap)) {
            _alignment1.push('-');
            _alignment2.push(_nuc2);
            j -= 1;
        } else if score.eq(&(score_up + _gap)) {
            _alignment1.push(_nuc1);
            _alignment2.push('-');
            i -= 1;
        }
    }

    while i > 0 {
        let _nuc1 = _seq1[i - 1];
        _alignment1.push(_nuc1);
        i -= 1;
    }

    while j > 0 {
        let _nuc2 = _seq2[j - 1];
        _alignment2.push(_nuc2);
        j -= 1;
    }

    //Para invertir el alineamiento
    _alignment1.reverse();
    _alignment2.reverse();

    let mut result: Vec<String> = Vec::new();

    let _ali1: String = _alignment1.into_iter().collect();
    result.push(_ali1);
    let _ali2: String = _alignment2.into_iter().collect();
    result.push(_ali2);

    result
}

fn getScore(_alignment: Vec<String>, _mach: i32, _gap: i32, _mismatch: i32) -> i32 {
    let _alignment1: Vec<char> = _alignment[0].chars().collect();
    let _alignment2: Vec<char> = _alignment[1].chars().collect();

    let length = _alignment1.len();

    let mut score = 0;

    for i in 0..length {
        if _alignment1[i] != _alignment2[i] {
            score += _mismatch;
        } else if _alignment1[i] == _alignment2[i] {
            score += _mach;
        } else {
            score += _gap;
        }
    }
    score
}
