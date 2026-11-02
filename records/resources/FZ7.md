---
records:
    - id: FZ7XKXJ2VP
      kind: monograph
      title: Mathematical Tapas
      creators:
        - name: Jean-Baptiste Hiriart-Urruty
          role: author
      date: "2016"
      msc:
        - code: 00A07
          from: zbmath_search
        - code: 97U40
          from: zbmath_search
        - code: 15-01
          from: zbmath_search
        - code: 26-01
          from: zbmath_search
        - code: 90-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2016"
          ids:
            doi:
                - 10.1007/978-3-319-42186-5
                - 10.1007/978-3-319-68631-8
            zbl: "1388.00010"
            zbl_id: "6811232"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2016"
              ids:
                isbn:
                    - "9783319421858"
                    - "9783319421865"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer International Publishing
              date: "2017"
              ids:
                isbn:
                    - "9783319686301"
                    - "9783319686318"
              access:
                class: record
      relations:
        - kind: part_of
          to: 3YXAC8SZBF
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.17 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-42186-5
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-68631-8
          level: work
        - source: zbmath_search
          snapshot: blake3:ba52b67aca79888bd54f4ac0d57bd446df8c82ca03dd9e92e0bc9db1402905ce
          native_id: "6811232"
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
          by: m2 v0.6.17 scope/1
          note: from in to in
---
