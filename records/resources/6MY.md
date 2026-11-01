---
records:
    - id: 6MYXVXWZPD
      kind: monograph
      title: 'A History of Abstract Algebra: From Algebraic Equations to Modern Algebra'
      creators:
        - name: Jeremy Gray
          role: author
      date: "2018"
      msc:
        - code: 01-02
          from: zbmath_search
        - code: 01A05
          from: zbmath_search
        - code: 12-03
          from: zbmath_search
        - code: 11-03
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2018"
          ids:
            doi: 10.1007/978-3-319-94773-0
            zbl: "1411.01005"
            zbl_id: "6908775"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2018"
              ids:
                isbn:
                    - "9783319947723"
                    - "9783319947730"
              access:
                class: record
      relations:
        - kind: part_of
          to: 3YXAC8SZBF
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-94773-0
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "6908775"
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
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
