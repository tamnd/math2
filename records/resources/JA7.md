---
records:
    - id: JA71N556X7
      kind: problem-set
      title: Kvant 2003, no. 2
      date: "2003"
      expressions:
        - key: e1
          kind: edition
          date: "2003"
          structure: JA71N556X7/e1.json
      relations:
        - kind: part_of
          to: W84MAFPC23
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: kvant
          snapshot: blake3:9ef7ec326c8e38c2cc1957ddca07480f15b4e9ef49d8059191fc4a1c78c7cd39
          native_id: 2003-2
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: JA7R8KNHBP
      kind: monograph
      title: Compactifying Moduli Spaces for Abelian Varieties
      creators:
        - name: Martin C. Olsson
          role: author
      date: "2008"
      msc:
        - code: 14-02
          from: zbmath_search
        - code: 14Kxx
          from: zbmath_search
        - code: 14K10
          from: zbmath_search
        - code: 14K25
          from: zbmath_search
        - code: 14A20
          from: zbmath_search
        - code: 14M25
          from: zbmath_search
        - code: 14F10
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2008"
          ids:
            doi: 10.1007/978-3-540-70519-2
            zbl: "1165.14004"
            zbl_id: "5306366"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2008"
              ids:
                isbn:
                    - "9783540705185"
                    - "9783540705192"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-540-70519-2
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "5306366"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
