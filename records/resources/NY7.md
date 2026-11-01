---
records:
    - id: NY7V3SM38K
      kind: monograph
      title: Dynamical Systems VII
      creators:
        - name: V. I. Arnol’d
          role: editor
        - name: S. P. Novikov
          role: editor
      date: "1993"
      msc:
        - code: 00B15
          from: zbmath_search
        - code: 58-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1993"
          ids:
            doi:
                - 10.1007/978-3-662-06796-3
                - 10.1007/978-3-662-06798-7
            zbl: "0795.00013"
            zbl_id: "49014"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1994"
              ids:
                isbn:
                    - "9783642057380"
                    - "9783662067963"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1993"
              ids:
                isbn:
                    - "9783642081019"
                    - "9783662067987"
              access:
                class: record
      relations:
        - kind: part_of
          to: XGZPMQ7BSM
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-06796-3
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-06798-7
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "49014"
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
          by: m2 v0.6.14 scope/1
          note: from in to in
---
