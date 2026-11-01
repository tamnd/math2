---
records:
    - id: NVF088HX12
      kind: monograph
      title: Probability Essentials
      creators:
        - name: Jean Jacod
          role: author
        - name: Philip Protter
          role: author
      date: "2000"
      msc:
        - code: 60-01
          from: zbmath_search
        - code: "60E05"
          from: zbmath_search
        - code: "60E10"
          from: zbmath_search
        - code: 60G42
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2000"
          ids:
            doi:
                - 10.1007/978-3-642-51431-9
                - 10.1007/978-3-642-55682-1
            zbl: "0968.60003"
            zbl_id: "1391230"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2000"
              ids:
                isbn:
                    - "9783540664192"
                    - "9783642514319"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2004"
              ids:
                isbn:
                    - "9783540438717"
                    - "9783642556821"
              access:
                class: record
      relations:
        - kind: part_of
          to: W0CC03QJC7
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-642-51431-9
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-642-55682-1
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "1391230"
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
