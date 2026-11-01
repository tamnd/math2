---
records:
    - id: GMAKX9NYXW
      kind: monograph
      title: Nombres Transcendants
      creators:
        - name: Michel Waldschmidt
          role: author
      date: "1974"
      msc:
        - code: 11J81
          from: zbmath_search
        - code: 11-01
          from: zbmath_search
        - code: 11J61
          from: zbmath_search
        - code: 30C15
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: fr
          date: "1974"
          ids:
            doi: 10.1007/bfb0065320
            zbl: "0302.10030"
            zbl_id: "3472160"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1974"
              ids:
                isbn:
                    - "9783540068747"
                    - "9783540378365"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0065320
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3472160"
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
