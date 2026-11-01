---
records:
    - id: 7QEGRM5AP9
      kind: monograph
      title: Computational Invariant Theory
      creators:
        - name: Harm Derksen
          role: author
        - name: Gregor Kemper
          role: author
      date: "2002"
      msc:
        - code: 13A50
          from: zbmath_search
        - code: 13P10
          from: zbmath_search
        - code: 13H10
          from: zbmath_search
        - code: 13-02
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2002"
          ids:
            doi:
                - 10.1007/978-3-662-04958-7
                - 10.1007/978-3-662-48422-7
            zbl: "1011.13003"
            zbl_id: "1764948"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2002"
              ids:
                isbn:
                    - "9783642077968"
                    - "9783662049587"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2015"
              ids:
                isbn:
                    - "9783662484203"
                    - "9783662484227"
              access:
                class: record
      relations:
        - kind: part_of
          to: XGZPMQ7BSM
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-04958-7
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-48422-7
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "1764948"
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
