---
records:
    - id: 2HWVBTBJAB
      kind: monograph
      title: Séminaire de Probabilités VIII Université de Strasbourg
      creators:
        - name: C. Dellacherie
          role: author
        - name: P.A. Meyer
          role: author
        - name: M. Weil
          role: author
      date: "1974"
      msc:
        - code: 00Bxx
          from: zbmath_search
        - code: 60-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: fr
          date: "1974"
          ids:
            doi: 10.1007/bfb0057249
            zbl: "0277.00015"
            zbl_id: "3435438"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1974"
              ids:
                isbn:
                    - "9783540067832"
                    - "9783540383840"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 dev scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0057249
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "3435438"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-02"
          by: m2 dev scope/1
          note: from in to in
---
